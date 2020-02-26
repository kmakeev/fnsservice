'use strict';
    angular
        .module('myApp')
        .controller('myCtrlRequests', function myCtrlRequests($scope, $location, Request) {
            console.log('In add profileCtrl');

            $scope.section = {
                            "all": true,
                            "process": false,
                            "resolved": false,
                            "archive": false
                            };

            $scope.input_requests = undefined;
            var param = function (page)
            {
                this.page = page;
            }
            var input_param = new param(1);
            input_param.code = 'all';

            var input_requests = new Request(input_param);
            $scope.input_requests_promise = input_requests.getRequests();
            $scope.input_requests_promise.then(function(result) {
                    console.log('requests - ', result);
                    $scope.input_requests = result;
                        })
                        .catch(function(result){
                    console.log('Error in get json data');
                    $scope.input_request = undefined;
                    });
            $scope.setPage = function(page) {

                input_param.page = page;
                input_requests.setPage(input_param);
                $scope.input_requests_promise = input_requests.getRequests();
            }

            $scope.setSection = function(name) {
                console.log('In set section');
                //var code = '';
                //var idreq = undefined;
                for (var s in $scope.section){
                    s == name ? $scope.section[s] = true : $scope.section[s] = false;
                }

                /*
                switch(name) {
                        case 'all':
                            code = 'all';
                            idreq = false;
                            break;
                        case 'process':
                            code = '52';
                            break;
                        case 'resolved':
                            code = '01';
                            break;
                        default:
                            code ='';
                    }
                */
                    input_param.code = name;
                    //input_param.idreq = idreq;
                    input_requests.setPage(input_param);
                    $scope.input_requests_promise = input_requests.getRequests();
            }

        });