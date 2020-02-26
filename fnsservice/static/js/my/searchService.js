'use strict';
    angular
        .module('myApp')
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
        });