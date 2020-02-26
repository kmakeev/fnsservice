'use strict';
    angular
        .module('myApp', ['ngRoute', 'ngAnimate', 'ngSanitize', 'ngResource', 'ngParseExt', 'dadata', 'cgBusy', 'djng.websocket'])
        .config(function($interpolateProvider, $locationProvider, $routeProvider, $httpProvider, $resourceProvider, djangoWebsocketProvider) {
            console.log('In change config');
            $interpolateProvider.startSymbol('{$');
            $interpolateProvider.endSymbol('$}');
            $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
            $resourceProvider.defaults.stripTrailingSlaches = false;

            djangoWebsocketProvider.setURI('ws://myesys.ru/ws/');
            djangoWebsocketProvider.setHeartbeat('--heartbeat--');
            djangoWebsocketProvider.setLogLevel('debug');
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
                .when('/requests', {
                    templateUrl: 'view/requests.html',
                    controller: 'myCtrlRequests'
                })
                .otherwise( {
                    redirectTo: '/'
                })
            });

