// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
angular.module('MyApp', ['ionic'])

.controller('MyCtrl', function($scope,$ionicLoading,$state) {
  
  
  $scope.arriver = function(item) {
	var date = new Date();
	alert('Arrivée de '+ item.nom + ' à '+ date.getHours()+"h "+date.getMinutes()+"min "+date.getSeconds()+"s");
  };
  $scope.sortir = function(item) {
	var date = new Date();
    alert('Sortie de '+ item.nom + ' à '+ date.getHours()+"h "+date.getMinutes()+"min "+date.getSeconds()+"s");
  };
  
  $scope.plus = function(item) {
	var nom=item.nom
	var age=item.age
	var classe=item.classe
	$state.go('fiche',{nom : nom,age : age, classe : classe});
  };
  
  $scope.enfants = [{
						"nom":"Martin",
						"age": 12,
						"classe":"CE2"
					},
					{
						"nom":"Carla",
						"age": 13,
						"classe":"CP"
					},
					{
						"nom":"Louis",
						"age": 6,
						"classe":"CM2"
					},
					
					{
						"nom":"Noemie",
						"age": 8,
						"classe":"CP"
					},
					{
						"nom":"David",
						"age": 11,
						"classe":"CP"
					}
		];
  
})

.controller('FicheCtrl', function($scope,$ionicLoading,$state,$stateParams) {
	 $scope.nom = $stateParams.nom;
	 $scope.classe = $stateParams.classe;
	 $scope.age = $stateParams.age;
})

.config(function($stateProvider,$urlRouterProvider){
		$urlRouterProvider.otherwise('/home')
		$stateProvider
			.state('home',{
			url:'/home',
			templateUrl:'pages/home.html',
			controller : 'MyCtrl'})
			.state('fiche',{
			url:'/fiche/:nom/:classe/:age',
			templateUrl:'pages/fiche.html',
			controller : 'FicheCtrl'})
})

.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
    // for form inputs).
    // The reason we default this to hidden is that native apps don't usually show an accessory bar, at
    // least on iOS. It's a dead giveaway that an app is using a Web View. However, it's sometimes
    // useful especially with forms, though we would prefer giving the user a little more room
    // to interact with the app.
    if (window.cordova && window.cordova.plugins.Keyboard) {
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
      cordova.plugins.Keyboard.disableScroll(true);
    }
    if (window.StatusBar) {
      // Set the statusbar to use the default style, tweak this to
      // remove the status bar on iOS or change it to use white instead of dark colors.
      StatusBar.styleDefault();
    }
  });
});
