'use strict';
    angular
        .module('myApp')
         .controller('userCtrl', function myCtrlMenu($scope, $location, $http, User, djangoWebsocket) {
            console.log('In add userCtrl');

            djangoWebsocket.connect($scope, 'ws_user', 'ws_user', ['subscribe-user', 'publish-user']);
            $scope.ws_user ={};
            $scope.user = undefined;
            $scope.isInvalid = false;
            // $scope.user = User.getUser();
            var user = new User();
            $scope.user_promise = user.getUser();
            $scope.user_promise.then(function(result) {
                    console.log('In get user promise', result);
                    $scope.user = result;
                }).catch(function(result){
                    console.log('Error get auth user');
                    $scope.user = undefined;
                    });

            $scope.logout = function(){
                user.$logout();
                console.log('In logout user');
                $scope.user = undefined;
                $scope.ws_user ={};
                $location.path('/');
                };


            $scope.submit = function() {
                console.log('In post login');
                if ($scope.subscribe_data) {
                    $http.post("/", $scope.subscribe_data).then(successCallback, errorCallback);
                } else {
                    $scope.errors = ['Необходимо указать имя пользователя и пароль'];
                    $scope.isInvalid = true;
                }
                return false;
            };
            function successCallback(out_data){
                                console.log('in login result');
                                if (!out_data.data.errors.__all__){
                                $scope.isInvalid = false;
                                $scope.user_promise = user.getUser();
                                $scope.user_promise.then(function(result) {
                                    console.log('In get user promise', result);
                                    $scope.user = result;
                                    $('#loginModal').modal('hide')

                                });

                               // $location.path('/');
                                } else {
                                console.log('password error');
                                $scope.isInvalid = true;
                                $scope.errors = out_data.data.errors.__all__;
                                }
                      }
            function errorCallback(out_data){
                                //error code
                                console.error('An error occured during submission');
                                $scope.errors = ['Системная ошибка'];
                                $scope.isInvalid = true;
                                //$scope.errors = out_data.data.errors;
                      }


        });
