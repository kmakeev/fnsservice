'use strict';
    angular
        .module('myApp')
        .controller('myCtrlDashboard', function myCtrlDashboard($scope, $route, $routeParams, $location, $anchorScroll, $http, Documents) {
            console.log('In add myCtrlDashboard');
            $scope.content = [{
                            "title": "Начало",
                            "href": "top",
                            "href_test": "top"
                            },
                            {
                                "title": "Сведения о ФЛ, являющихся руководителями (участниками) нескольких юридических лиц",
                                "href": "title1",
                                "href_test": "title1"
                            },
                            {
                                "title": "Юридические лица, созданные по законодательству Украины, сведения о которых внесены в ЕГРЮЛ",
                                "href": "title2",
                                "href_test": "title2"
                            },
                            {
                                "title": "Юридические лица, в состав исполнительных органов которых входят дисквалифицированные лица",
                                "href": "title3",
                                "href_test": "title3"
                            },
                            {
                                "title": "Конец",
                                "href": "bottom",
                                "href_test": "bottom"
                            }];
            var param = function (page)
            {
                this.page = page;
            }
            var UK_param = new param(1);
            UK_param.codeEduMethod = "03";
            //UK_param.СвЮЛ__СведДолжнФЛ__СвДискв__isnull = null;
            // console.log('UK_param - ', UK_param);
            var filter_uk = new Documents(UK_param);
            $scope.vm_promise2 = filter_uk.retrieveFilter();
            $scope.vm_promise2.then(function(result) {
                    $scope.vm2 = result;
                        })
                    .catch(function(result){
                    console.log('Error in get json data');
                    });


           // $scope.vm_value = $scope.vm.$$state.value();
            $scope.setPage2 = function(page) {
                // console.log('UK_param - ', UK_param);
                UK_param.page = page;
                //UK_param.СвЮЛ__СвОбрЮЛ__СпОбрЮЛ__КодСпОбрЮЛ = "03";
                filter_uk.setPage(UK_param);
                $scope.vm_promise2 = filter_uk.retrieveFilter();
            }

            var Disq_param = new param(1);
            Disq_param.disqualification = false;
           // Disq_paramСвЮЛ__СвОбрЮЛ__СпОбрЮЛ__КодСпОбрЮЛ = null;
            // console.log('Disc_param - ', Disq_param);

            var filter_disq = new Documents(Disq_param);
            $scope.vm_promise = filter_disq.retrieveFilter();
            $scope.vm_promise.then(function(result) {
                    $scope.vm = result;
                        })
                    .catch(function(result){
                    console.log('Error in get json data');
                    });


           // $scope.vm_value = $scope.vm.$$state.value();
            $scope.setPage = function(page) {
                Disq_param.page = page;
                filter_disq.setPage(Disq_param);
                $scope.vm_promise = filter_disq.retrieveFilter();
            }

            $scope.scrollTo = function(id){
            console.log('In scroll');
            console.log(id);
            $anchorScroll.yOffset = 55;
            $anchorScroll(id);            }

        });