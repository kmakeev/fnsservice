'use strict';
    angular
        .module('myApp', ['ngRoute', 'ngAnimate', 'dadata'])
        .config(function($interpolateProvider, $locationProvider, $routeProvider) {
            console.log('In change config');
            $interpolateProvider.startSymbol('{$');
            $interpolateProvider.endSymbol('$}');
            $locationProvider.hashPrefix('!');
            $routeProvider
                .when('/start', {
                    templateUrl: 'partails/start.html'
                })
                .when('/', {
                    templateUrl: 'partails/index.html'

                })
                .otherwise( {
                    redirectTo: 'partails/index.html'
                    })

            })

        .controller('myCtrl', function myCtrl($scope) {
            console.log('In add Ctrl');
            $scope.hello = 'AngularJS';
            })
        .run(['dadataConfig', function(dadataConfig) {
            dadataConfig.token = '7506f3a57073d950b559309bcab0288df215ba7b';
            dadataConfig.timeout = 3000;
            }]);