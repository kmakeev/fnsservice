'use strict';
    angular
        .module('myApp')
        .factory ('Documents', ['$resource', '$filter',
            function($resource, $filter) {
            //console.log('In factory filter -', $filter('date')('2017-12-31T21:00:00.000Z', 'yyyy-MM-dd'));

            var resource =
             $resource("/api/documents/", {
             },
             {
               listquery: {
                    method: 'GET',
                    timeout: 300000,
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
        }]);