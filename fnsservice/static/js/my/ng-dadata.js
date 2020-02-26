
/* global angular, $ */
;(function () {
  'use strict';

  angular
    .module('dadata', [])
    .directive('dadata', [function () {
      function link (scope, element) {
        $(element).suggestions({
          serviceUrl: 'https://suggestions.dadata.ru/suggestions/api/4_1/rs',
          token: '7506f3a57073d950b559309bcab0288df215ba7b',
          type: scope.type.toUpperCase(),
          autoSelectFirst: "True",
          onSelect: function(suggestion) {
            scope.data = suggestion.data;
            scope.$apply();
          }
        });
      }

      return {
        restrict: 'A',
        link: link,
        scope: {
          type: '@ddtType',
          data: '=ddtModel'
        }
      };

    }]);

})();


