/*!
 * dadata-suggestions-angular
 * https://github.com/Softmotions/dadata-suggestions-angular
 * Version: 0.0.2 - 2016-07-26T12:00:00.000Z
 * License: MIT
 */

/**
 *  Директива для проверки данных через сервис DaData.ru. Подсказки включаются при первой попытке изменить содержимое
 *  полей (иначе можно запортить значения, а пользователь их не заметит).
 *  Требует dadataConfig.token = "<API-KEY>"
 *  Usage: <form dadata dadata-type="address" [dadata-auto-select-first="false"] [dadata-trigger-select-on-blur="true"]
 *          [dadata-trigger-select-on-enter="true"] [dadata-trigger-select-on-space="false"]>
 *             <input id="region" ng-model="region" dadata-input dadata-bounds="region">
 *             <input id="city" ng-model="city" dadata-input dadata-bounds="city" dadata-constraint-input-id="region" dadata-fixdata="true">
 *         </form>
 *
 *  Обязательные параметры:
 *      dadata: type - тип подсказок, см. https://confluence.hflabs.ru/display/SGTDOC165/API
 *      dadata-input: id, ng-model
 *  Настройки:
 *      auto-select-first - включает автовыбор первой подсказки по событиям. По-умолчанию выключено.
 *      trigger-select-on-[blur|enter|space] - автовыбор первой подсказки по событию.
 *          в примере указаны значения по-умолчанию.
 *      bounds - гранулярные подсказки http://codepen.io/dadata/pen/cGkah?editors=101
 *          ограничение на аттрибут для поиска, например city - поиск только городов.
 *          можно указать диапазон city-settlement - поиск по городу и населенному пункту.
 *          если указано только одно значение, то в поле ввода попадает только этот аттрибут,
 *          в противном случае - сырое значение возвращенное сервисом
 *      constraint-input-id - id поля ввода, значение которого должно учитываться для поиска.
 *          например, для поля ввода город нужно указать поле ввода региона
 *      fixdata == true - для последнего поля в цепочке гранулярных подсказок.
 *          необходимо, если в момент подключения подсказок в форме уже есть данные.
 *          автоматически добавляется для единственного поля.
 */
'use strict';

angular.module('dadataSuggestions', [])
    .value('dadataConfig', {
        token: false,
        timeout: 3000
    })
    .directive('dadata', ['$timeout', '$interval', function ($timeout, $interval) {
        return {
            restrict: 'A',
            scope: {
                type: '@dadataType',
                autoSelectFirst: '@dadataAutoSelectFirst',
                triggerSelectOnBlur: '@dadataTriggerSelectOnBlur',
                triggerSelectOnEnter: '@dadataTriggerSelectOnEnter',
                triggerSelectOnSpace: '@dadataTriggerSelectOnSpace'
            },
            controller: ['$scope', function ($scope) {
                var inputs = $scope.inputs = {};
                this.addInput = function (name, input) {
                    inputs[name] = input;
                };
                this.inputs = $scope.inputs;
                this.type = $scope.type;

                // set default values
                this.autoSelectFirst = $scope.autoSelectFirst || false;
                this.triggerSelectOnBlur = $scope.triggerSelectOnBlur || true;
                this.triggerSelectOnEnter = $scope.triggerSelectOnEnter || true;
                this.triggerSelectOnSpace = $scope.triggerSelectOnSpace || false;
            }],
            link: function (scope) {
                $timeout(function () {
                    var isEmpty = true;
                    var inputsLength = 0;
                    angular.forEach(scope.inputs, function (input) {
                        if (input.ngModel) {
                            isEmpty = false;
                        }
                        input.prevValue = input.ngModel;
                        inputsLength++;
                    });

                    // auto-enable fixData on non-granular suggestions
                    if (inputsLength == 1) {
                        angular.forEach(scope.inputs, function (input) {
                            input.fixdata = true;
                        });
                    }

                    // check for empty form
                    angular.forEach(scope.inputs, function (input) {
                        if (isEmpty) { // form is empty - disable fixData
                            input.fixdata = false;
                        } else { // form is not empty - disable suggestions util user try to modify values
                            var inputSelector = $("#" + input.id);
                            var timer = $interval(function () {
                                if (inputSelector.suggestions().isInitialized()) {
                                    inputSelector.suggestions().disable();
                                    $interval.cancel(timer);
                                }
                            }, 100);
                        }
                    });
                });
            }
        };
    }])
    .directive('dadataInput', ['dadataConfig', '$timeout', function (dadataConfig, $timeout) {
        return {
            restrict: 'A',
            require: '^^dadata',
            scope: {
                ngModel: '=',
                id: '@',
                bounds: '@dadataBounds',
                constraintInputId: '@dadataConstraintInputId',
                fixdata: '@dadataFixdata',
                prevValue: '@'
            },
            link: function (scope, iElement, iAttrs, parentCtrl) {
                // require defined token, type, ng-model and id
                if (dadataConfig.token && iAttrs['ngModel'] && iAttrs['id'] && parentCtrl.type) {
                    parentCtrl.addInput(iAttrs['ngModel'], scope);
                    iElement.suggestions({
                        serviceUrl: "https://suggestions.dadata.ru/suggestions/api/4_1/rs",
                        token: dadataConfig.token,
                        type: parentCtrl.type.toUpperCase(),
                        timeout: dadataConfig.timeout,
                        autoSelectFirst: parentCtrl.autoSelectFirst,
                        triggerSelectOnBlur: parentCtrl.triggerSelectOnBlur,
                        triggerSelectOnEnter: parentCtrl.triggerSelectOnEnter,
                        triggerSelectOnSpace: parentCtrl.triggerSelectOnSpace,
                        bounds: scope.bounds || '',
                        constraints: (scope.constraintInputId) ? $('#' + scope.constraintInputId) : '',
                        formatSelected: function (suggestion) {
                            if (scope.bounds && (scope.bounds.search(/^\w+$/) != -1)) { // dadataBounds can contain range of attributes
                                return eval('suggestion.data.' + scope.bounds); // bounds contain only one attribute - return value of selected attribute
                            }
                            return suggestion.value;
                        }
                    });

                    iElement.bind('suggestions-clear suggestions-select suggestions-set', function (event) { // update model after jquery
                        var ngModelToSet = event.target.attributes['ng-model'].value;
                        parentCtrl.inputs[ngModelToSet].prevValue = event.target.value;
                        parentCtrl.inputs[ngModelToSet].ngModel = event.target.value;
                    });

                    iElement.bind('suggestions-fixdata', function () { // enable suggestions after fixData complete
                        angular.forEach(parentCtrl.inputs, function (input) { // refresh model on whole form after jquery
                            var inputSelector = $("#" + input.id);
                            inputSelector.suggestions().enable();
                            input.ngModel = inputSelector.val();
                        });
                    });

                    var defaultModifyHandler = function (event) { // only keep model up-to-date
                        var ngModelToSet = event.target.attributes['ng-model'].value;
                        var input = parentCtrl.inputs[ngModelToSet];

                        function updateModel() {
                            if (input.prevValue != input.ngModel) {
                                input.prevValue = input.ngModel;
                                input.ngModel = event.target.value;
                            }
                        }
                        if (event.type == 'paste') {
                            $timeout(updateModel());
                        } else {
                            updateModel();
                        }
                    };

                    var modifyHandlerBeforeFixData = function (event) { // user try to modify values - we can check values in DaData
                        function cleanInput (id) {
                            angular.forEach(parentCtrl.inputs, function (input) {
                                if (input.constraintInputId == id) {
                                    $('#' + input.id).val("");
                                    cleanInput(input.id);
                                }
                            });
                        }

                        var ngModelToCheck = event.target.attributes['ng-model'].value;
                        var input = parentCtrl.inputs[ngModelToCheck];

                        function updateModelNRunFixData() {
                            if (input.prevValue != input.ngModel) { // run fixData on input value change
                                input.prevValue = input.ngModel;
                                if (!input.fixdata) {
                                    cleanInput(input.id); // must clean all granular fields with constraintInputId == input.id
                                }
                                angular.forEach(parentCtrl.inputs, function (input) {
                                    var inputSelector = $("#" + input.id);
                                    if (input.fixdata) {
                                        inputSelector.suggestions().fixData(); // run fixData on first try
                                        input.fixdata = false;
                                    }
                                    inputSelector.unbind('keyup paste', modifyHandlerBeforeFixData); // don't need anymore
                                    inputSelector.bind('keyup paste', defaultModifyHandler); // replace with default modify handler
                                });
                            }
                        }

                        if (event.type == 'paste') { // run fixData after paste complete
                            $timeout(updateModelNRunFixData());
                        } else {
                            updateModelNRunFixData();
                        }
                    };

                    iElement.bind('keyup paste', modifyHandlerBeforeFixData);
                }
            }
        };
    }]);
