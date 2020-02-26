'use strict';
    angular
        .module('myApp')
        .controller('myCtrlMenu', function myCtrlMenu($scope, $location, $http) {
            console.log('In add myCtrlMenu');
            $scope.menu =[{}];
            $http.get("menu.html").then(successCallback, errorCallback);
            function successCallback(response){
                        console.log('success get menu');
                        // console.log(response);
                        //success code
                        $scope.menu = response.data;
                        }
             function errorCallback(error){
                        //error code
                        console.error('An error occured during submission');
                    }

            $scope.isActive = function(location){
                return location==$location.path();
            };

        });