'use strict';
    angular
        .module('myApp')
         .controller('myCtrlErgul', function myCtrlErgul($scope, $route, $location, $http, $sce, $anchorScroll, OGRN) {
            console.log('In myCtrlErgul', OGRN);
            $scope.html_egrul = '<b>  </b>';
            $scope.content = [{
                            "title": "Начало",
                            "href": "top"
                            },
                            {
                                "title": "Конец",
                                "href": "bottom"
                            }];
            $scope.id = "";
            $scope.scrollTo = function(id){
                console.log('In scroll');
                console.log(id);
                $anchorScroll.yOffset = 55;
                $anchorScroll(id);
            }

            $scope.printDiv = function(divName){
                console.log('In Print');
                var printContents = document.getElementById(divName).innerHTML;
                var popupWin = window.open('Печать', '_blank', 'width=auto,height=auto');
                popupWin.document.open();
                popupWin.document.write('<html><head><link rel="stylesheet" type="text/css" href="style.css" /></head><body onload="window.print()">' + printContents + '</body></html>');
                popupWin.document.close();
            }

            $scope.getOrdering = function(){
                console.log('In getOrdering');
                if ($scope.getOrdering_data) {
                       $http.put("view/egrul.html", $scope.getOrdering_data).then(function (response){
                            console.log('In accept get ordering');
                             console.log(response);
                             if (!response.data.errors.__all__) {
                                $scope.isGetOrderInvalid = false;
                                $('#getOrderindModal').modal('hide')
                                $('#afterSendingModal').modal('show')
                             } else {
                                console.log('ret ordering error');
                                $scope.isGetOrderInvalid = true;
                                $scope.errors = response.data.errors.__all__;
                                }

                       }).catch(function (response) {
                            console.log('Error occurred get ordering', response);
                            $scope.errors = ['Системная ошибка'];
                            $scope.isGetOrderInvalid = true;
                       });
                }

            }
            $scope.isGetOrderInvalid = false;
            $scope.isDjForm = !$scope.showPopup;
            $scope.isInvalid = false;
            $scope.title = OGRN;
            $scope.subscribe_data = {'search': OGRN};
            $scope.getOrdering_data = {'search': OGRN,
                                       'type': 'fo'};

            // $scope.search = OGRN;
            $scope.errors = '';

            $scope.savePDF = function() {
                console.log(' in save PDF');

            }
            function successCallback(response){
                                //success code
                                console.log(' in callback');
                                if (response.data.find_errors.length==0) {
                                    console.log('response send valid');
                                    //console.log(response.data.goToSearch);
                                    if (!response.data.goToSearch) {
                                        console.log('Not go to search');
                                        $scope.isInvalid = false;
                                        // console.log(response.data.html_egrul);
                                        $scope.html_egrul = $sce.trustAsHtml(response.data.html_egrul);
                                        $scope.content = response.data.content;
                                        $scope.errors = response.data.find_errors;
                                        $scope.id = response.data.id;
                                    } else {
                                    //console.log('Go to search');
                                    console.log($scope.subscribe_data.search);
                                    //console.log(response.data.search_param);
                                    //$rootScope.searchparam = response.data.search_param;
                                    searchService.setSearch($scope.subscribe_data.search);
                                    searchService.setGoToSearch(true);
                                    $location.path('/search');
                                    //$scope.$emit('goToSearch');
                                    }


                                } else {
                                    console.log('response send invalid');
                                    $scope.isInvalid = true;
                                    $scope.errors = response.data.find_errors;
                                    $scope.html_egrul = '<b>  </b>';
                                }

                         }
                        function errorCallback(error){
                                //error code
                                console.error('An error occured during submission');
                                $scope.isInvalid = true;
                                $scope.errors = ["Отсутсвуют сведения для заданных параметров поиска. "];
                                $scope.html_egrul = '<b>  </b>';
                            }

            $scope.checkboxChange = function() {
                $scope.isDjForm = !$scope.showPopup;
                }

                $scope.submit = function() {
                console.log('In Submit');

                if (($scope.subscribe_data && $scope.isDjForm) || ($scope.party && !$scope.isDjForm)) {
                     console.log('yes data');
                     if ($scope.isDjForm) {
                        console.log('In isDjForm');
                        $http.post("view/egrul.html", $scope.subscribe_data).then(successCallback, errorCallback);
                     } else {
                        console.log('In isDadata');
                        console.log($scope.party.ogrn);
                            if ($scope.party.ogrn) {
                                var param = JSON.stringify({search:$scope.party.ogrn})
                                console.log(param);
                                $http.post("view/egrul.html",param).then(successCallback, errorCallback);
                            }
                     }
                } else {
                console.log('param for search invalid');
                // console.log($scope);
                $scope.isInvalid = true;
                $scope.errors = ['Параметр для поиска должен быть более одного символа'];
                return false;
                }
            };
            if ($scope.subscribe_data.search) {
                $scope.submit();
                }
        });
