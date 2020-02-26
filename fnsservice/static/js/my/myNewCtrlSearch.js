'use strict';
    angular
        .module('myApp')
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
                    $('#errorModal').modal('show')
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

        });