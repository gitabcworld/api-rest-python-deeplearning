'use strict';

var app = angular.module('app',[]);




app.config(['$interpolateProvider',
	function($interpolateProvider) {
		$interpolateProvider.startSymbol('[[');
		$interpolateProvider.endSymbol(']]');
	}]);


app.directive('fileModel',['$parse', function($parse) {
		return  {
			restrict: 'A',
			link: function(scope, element, attrs) {
				var model = $parse(attrs.fileModel)
				var modelSetter = model.assign;
				element.bind('change', function() {
				scope.$apply(function () {
					modelSetter(scope,element[0].files[0]);
				});
				
			});

		 }
			
		};
		
}]);


function logEvent(str) {
	console.log(str);
	var d = document.createElement('div');
	d.innerHTML = str;
	document.getElementById('result').appendChild(d);
}
function objToString(obj) {
	var str = '';
	for (var p in obj) {
		if (obj.hasOwnProperty(p)) {
			str+=p+'::'+obj[p]+'\n';
		}
	}
}

app.service('fileUpload',['$http', 
	function($http) {
		this.uploadFileToUrl = function(file) {
			var fd = new FormData();
			fd.append('file',file);
			$http.post('/photos/v1.0/photos',fd, {
				transformRequest: angular.identity,
				headers: {'Content-Type': undefined }
			})
			.success(function(responseid) {
				logEvent(JSON.stringify(responseid));
			})
			.error(function() {
			});
			
	};
}]);



app.controller('myController', ['$scope', 'fileUpload',
		function($scope,fileUpload) {
			$scope.uploadFile = function () {
				var file1 = $scope.myFile1;
				console.log('File is ');
				console.dir(file1);
				var uploadUrl = "/fileUpload";
				fileUpload.uploadFileToUrl(file1);
			};
		
}]);
