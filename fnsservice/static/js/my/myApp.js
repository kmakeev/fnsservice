'use strict';
    angular
        .module('myApp', ['ngRoute', 'ngAnimate', 'ngSanitize', 'ngResource', 'ngParseExt', 'dadata', 'cgBusy'])
        .config(function($interpolateProvider, $locationProvider, $routeProvider, $httpProvider, $resourceProvider) {
            console.log('In change config');
            $interpolateProvider.startSymbol('{$');
            $interpolateProvider.endSymbol('$}');
            $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
            $resourceProvider.defaults.stripTrailingSlaches = false;
            // optionally inform about the connection status in the browser's console
            $routeProvider
                .when('/', {
                    templateUrl: 'view/dashboard.html',
                    controller: 'myCtrlDashboard'

                })
                .when('/egrul/:OGRN', {
                    templateUrl: 'view/egrul.html',
                    controller: 'myCtrlErgul',
                    resolve: {
                        OGRN: function ($route) {
                        return $route.current.params.OGRN;
                        }
                    }

                })
                .when('/egrul', {
                    templateUrl: 'view/egrul.html',
                    controller: 'myCtrlErgul',
                    resolve: {
                        OGRN: function () {
                        return "";
                        }
                    }
                })
                .when('/search/', {
                    templateUrl: 'view/rest_search.html',
                    controller: 'myNewCtrlSearch'

                })
                .when('/profile', {
                    templateUrl: 'view/profile.html',
                    controller: 'userCtrl'
                })
                .otherwise( {
                    redirectTo: '/'
                })
                .otherwise( {
                    redirectTo: '/'
                })

            })
        .service('searchService', function($resource){

            var goToSearch = false;
            var search = '';
            var result = $resource("view/search.html");
            var errors;

            return {
                goToSearch: function() {
                    return goToSearch;
                },
                setGoToSearch: function(value) {
                    goToSearch = value;
                },
                search: function() {
                    return search;
                },
                setSearch: function(value) {
                    search = value;
                },
                result: function(subscribe_data) {
                    console.log('post result');
                    console.log(subscribe_data);
                    var q = result.save(subscribe_data)
                    console.log(q);
                    return q;
                },
                setResult: function(value) {
                    result = value;
                },
                errors: function() {
                    return errors;
                },
                setErrors: function(value) {
                    errors = value;
                },
                isInvalid: function() {
                    return isInvalid;
                },
                setIsInvalid: function(value) {
                    isInvalid = value;
                },
                successCallback: function(response){
                                    //success code
                                    console.log(' in callback');
                                    if (response.data.find_errors.length==0) {
                                        console.log('response send valid');
                                        console.log(response.data.result);
                                        result = response.data.result;
                                        errors = response.data.find_errors;
                                        search = "TEST";
                                        console.log(self);


                                    } else {
                                        console.log('response send invalid');
                                        isInvalid = true;
                                        errors = response.data.find_errors;
                                    }

                             },
                errorCallback: function(response){
                                    //error code
                                    console.error('An error occured during submission');
                                    isInvalid = true;
                                    errors = response.data.find_errors;
                                }

            }


        }).factory ('Documents', ['$resource', '$filter',
            function($resource, $filter) {
            //console.log('In factory filter -', $filter('date')('2017-12-31T21:00:00.000Z', 'yyyy-MM-dd'));

            var resource =
             $resource("/api/documents/", {
             },
             {
               listquery: {
                    method: 'GET',
                    isArray: false
               },

             });
            resource.prototype.setPage  = function (param, filterParam) {
            console.log('In setPage -', param, filterParam);
            this.page = param.page;
            this.codeEduMethod = param.codeEduMethod;
            this.disqualification = param.disqualification;
            this.search = param.search;
            this.fio = param.fio;
            this.region = param.region;
            this.reg_start_date = $filter('date')(param.reg_start_date, 'yyyy-MM-dd');
            this.reg_end_date =  $filter('date')(param.reg_end_date, 'yyyy-MM-dd');
            this.state = param.state;
            this.isactive = param.isactive;
            this.okved = param.okved;

            if (filterParam) {
                this.isAddrFalsity = filterParam.isAddrFalsity;
                this.isAddrChange = filterParam.isAddrChange;
                this.isemail = filterParam.isemail;
                this.email = filterParam.email;
                this.index = filterParam.index;
                this.codeKLADR = filterParam.codeKLADR;
                this.area = filterParam.area;
                this.city = filterParam.city;
                this.locality = filterParam.locality;
                this.street = filterParam.street;
                this.codeEduMethod = filterParam.codeEduMethod.value;
                this.regNum = filterParam.regNum;
                this.startregDate = $filter('date')(filterParam.startregDate, 'yyyy-MM-dd');
                this.endregDate =  $filter('date')(filterParam.endregDate, 'yyyy-MM-dd');
                this.isChartCapital = filterParam.isChartCapital;
                this.nameCapital = filterParam.nameCapital.value;
                this.summCap = filterParam.summCap;
                this.isSvUprOrg = filterParam.isSvUprOrg;
                this.nameUprOrg = filterParam.nameUprOrg;
                this.isSvWithoutAtt = filterParam.isSvWithoutAtt;
                this.fioWA = filterParam.fioWA;
                this.isFounder = filterParam.isFounder;
                this.isFRus = filterParam.isFRus;
                this.isFFl = filterParam.isFFl;
                this.isFGOS = filterParam.isFGOS;
                this.isFIn = filterParam.isFIn;
                this.okvedtxt = filterParam.okvedtxt;
                this.numberL = filterParam.numberL;
                this.startLicense = $filter('date')(filterParam.startLicense, 'yyyy-MM-dd');
                this.endLicense =  $filter('date')(filterParam.endLicense, 'yyyy-MM-dd');
                this.nameL = filterParam.nameL;
                this.grn = filterParam.grn;
                this.startRecord = $filter('date')(filterParam.startRecord, 'yyyy-MM-dd');
                this.endRecord =  $filter('date')(filterParam.endRecord, 'yyyy-MM-dd');
                this.declarer = filterParam.declarer;
                this.documents = filterParam.documents;
                }

            };
            resource.prototype.retrieveFilter = function () {
               console.log('In retrieveFilter -', this.page,  this.search);
                return this.$listquery(
                {
                  codeEduMethod: this.codeEduMethod,
                  disqualification: this.disqualification,
                  search: this.search,
                  fio: this.fio,
                  region: this.region,
                  state: this.state,
                  page: this.page,
                  isactive: this.isactive,
                  reg_start_date: this.reg_start_date,
                  reg_end_date: this.reg_end_date,
                  isAddrFalsity: this.isAddrFalsity,
                  isAddrChange: this.isAddrChange,
                  isemail: this.isemail,
                  email: this.email,
                  index: this.index,
                  codeKLADR: this.codeKLADR,
                  area: this.area,
                  city: this.city,
                  locality: this.locality,
                  street: this.street,
                  regNum: this.regNum,
                  startregDate: this.startregDate,
                  endregDate: this.endregDate,
                  isChartCapital: this.isChartCapital,
                  nameCapital: this.nameCapital,
                  summCap: this.summCap,
                  isSvUprOrg: this.isSvUprOrg,
                  nameUprOrg: this.nameUprOrg,
                  isSvWithoutAtt: this.isSvWithoutAtt,
                  fioWA: this.fioWA,
                  isFounder: this.isFounder,
                  isFRus: this.isFRus,
                  isFFl: this.isFFl,
                  isFGOS: this.isFGOS,
                  isFIn: this.isFIn,
                  okved: this.okved,
                  okvedtxt: this.okvedtxt,
                  numberL: this.numberL,
                  startLicense: this.startLicense,
                  endLicense: this.endLicense,
                  nameL: this.nameL,
                  grn: this.grn,
                  startRecord: this.startRecord,
                  endRecord: this.endRecord,
                  declarer: this.declarer,
                  documents: this.documents


                });
            };
            return resource;
        }])
        .factory ('Filters', ['$resource',
            function($resource) {

            var resource =
             $resource("/api/filters/", {},
             {
               query: {
                    method: 'GET',
                    isArray: false
               },

             });

            return resource;
        }])
        .factory ('User', ['$resource',
            function($resource) {

            var resource =
             $resource("/api/user/", {},
             {
               query: {
                    method: 'GET',
                    isArray: false
               },
                logout: {
                    method: 'DELETE',
                    isArray: false
               },
             });
             resource.prototype.getUser = function () {
               console.log('In get User');
                return this.$query({});
            };
            return resource;
        }])

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

        })
        .controller('myNewCtrlSearch', function myCtrlSearch($scope, $http, $route, $location, $anchorScroll, searchService, Documents, Filters) {
            console.log('In add my NEW CtrlSearch');

            var set_filters = new Filters();

            set_filters.$query().then(function(result) {
                    $scope.advancedFilter = result.data;
                        });
            $scope.advanced_subscribe_data = {};
            $scope.subscribe_data = {};
            var filter = new Documents();

            $scope.submit = function() {
                console.log('In Submit');
                console.log($scope.subscribe_data);
                if ($scope.subscribe_data) {
                     console.log('yes params -', $scope.subscribe_data);
                     $scope.isInvalid = false;
                     $scope.subscribe_data.page = 1;
                     filter.setPage($scope.subscribe_data, $scope.advanced_subscribe_data);
                     $scope.search_promise = filter.retrieveFilter();
                     $scope.search_promise.then(function(result) {
                     $scope.search = result;
                        })
                    .catch(function(result){
                    console.log('Error in get json data');
                    });
                    // $scope.result = searchService.result($scope.subscribe_data);
                } else {
                console.log('param for search invalid');
                // console.log($scope);
                $scope.isInvalid = true;
                $scope.errors = ['Необходимо выбрать хотя бы один параметр поиска'];
                return false;
                }
            }
            $scope.setPage = function(page) {
                $scope.subscribe_data.page = page;
                filter.setPage($scope.subscribe_data, $scope.advanced_subscribe_dat);
                $scope.search_promise = filter.retrieveFilter();
                // $anchorScroll.yOffset = 55;
                // $anchorScroll('top');
            }
            $scope.resetParam = function() {
                console.log('Reset param - ');
                $scope.subscribe_data.search = undefined;
                $scope.subscribe_data.fio = undefined;
                $scope.subscribe_data.region = undefined;
                $scope.subscribe_data.state = undefined;
                $scope.subscribe_data.isactive = undefined;
                $scope.subscribe_data.reg_start_date = undefined;
                $scope.subscribe_data.reg_end_date = undefined;
                $scope.subscribe_data.okved = undefined;
            }
            $scope.resetFilterParam = function() {
                console.log('Reset filter param - ');
                $scope.advanced_subscribe_data.isAddr = undefined;
                $scope.advanced_subscribe_data.isAddrFalsity = undefined;
                $scope.advanced_subscribe_data.isAddrChange = undefined;
                $scope.advanced_subscribe_data.isemail = undefined;
                $scope.advanced_subscribe_data.email = undefined;
                $scope.advanced_subscribe_data.index = undefined;
                $scope.advanced_subscribe_data.codeKLADR = undefined;
                $scope.advanced_subscribe_data.area = undefined;
                $scope.advanced_subscribe_data.city = undefined;
                $scope.advanced_subscribe_data.locality = undefined;
                $scope.advanced_subscribe_data.street = undefined;
                $scope.advanced_subscribe_data.isRegInfo = undefined;
                $scope.advanced_subscribe_data.codeEduMethod = "";
                $scope.advanced_subscribe_data.regNum = undefined;
                $scope.advanced_subscribe_data.startregDate = undefined;
                $scope.advanced_subscribe_data.endregDate = undefined;
                $scope.advanced_subscribe_data.isChartCapital = undefined;
                $scope.advanced_subscribe_data.nameCapital = "";
                $scope.advanced_subscribe_data.summCap = undefined;
                $scope.advanced_subscribe_data.isSvUprOrg = undefined;
                $scope.advanced_subscribe_data.nameUprOrg = undefined;
                $scope.advanced_subscribe_data.isSvWithoutAtt = undefined;
                $scope.advanced_subscribe_data.fioWA = undefined;
                $scope.advanced_subscribe_data.isFounder = undefined;
                $scope.advanced_subscribe_data.isFRus = undefined;
                $scope.advanced_subscribe_data.isFFl = undefined;
                $scope.advanced_subscribe_data.isFGOS = undefined;
                $scope.advanced_subscribe_data.isFIn = undefined;
                $scope.advanced_subscribe_data.isOKVED = undefined;
                $scope.advanced_subscribe_data.okvedtxt = undefined;
                $scope.advanced_subscribe_data.isLicense = undefined;
                $scope.advanced_subscribe_data.numberL = undefined;
                $scope.advanced_subscribe_data.startLicense = undefined;
                $scope.advanced_subscribe_data.endLicense = undefined;
                $scope.advanced_subscribe_data.nameL = undefined;
                $scope.advanced_subscribe_data.isRecord = undefined;
                $scope.advanced_subscribe_data.grn = undefined;
                $scope.advanced_subscribe_data.startRecord = undefined;
                $scope.advanced_subscribe_data.endRecord = undefined;
                $scope.advanced_subscribe_data.declarer = undefined;
                $scope.advanced_subscribe_data.documents = undefined;

            }

        })

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

        })
        .controller('userCtrl', function myCtrlMenu($scope, $location, $http, User) {
            console.log('In add userCtrl');


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


        })
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

            $scope.isDjForm = !$scope.showPopup;
            $scope.isInvalid = false;
            $scope.title = OGRN;
            $scope.subscribe_data = {'search': OGRN};

            // $scope.search = OGRN;
            $scope.errors = '';

            $scope.savePDF = function() {
                console.log(' in save PDF');

            }
            $scope.checkboxChange = function() {
                $scope.isDjForm = !$scope.showPopup;
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


