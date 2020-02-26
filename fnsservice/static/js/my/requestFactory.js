'use strict';
    angular
        .module('myApp')
        .factory ('Request', ['$resource', '$filter',
            function($resource, $filter) {
            //console.log('In factory filter -', $filter('date')('2017-12-31T21:00:00.000Z', 'yyyy-MM-dd'));

            var resource =
             $resource("/api/request/", {
             },
             {
               listquery: {
                    method: 'GET',
                    isArray: false
               },

             });
            resource.prototype.setPage  = function (param) {
            console.log('In setPage -', param);
            this.page = param.page;
            this.code = param.code;
            this.idreq = param.idreq;

            //this.reg_start_date = $filter('date')(param.reg_start_date, 'yyyy-MM-dd');
            //this.reg_end_date =  $filter('date')(param.reg_end_date, 'yyyy-MM-dd');
            };
            resource.prototype.getRequests = function () {
               console.log('In getRequests -', this.page,  this.idreq);
                return this.$listquery(
                {
                  page: this.page,
                  code: this.code,
                  idreq: this.idreq
             });
            };
            return resource;
        }]);