// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
angular.module('MyApp', ['ionic', 'ngStorage'])

.factory ('StorageService', function ($localStorage) {

  $localStorage = $localStorage.$default({
    things: []
  });
  

  var _getAll = function () {
    return $localStorage.things;
  };

  var _add = function (thing) {
    $localStorage.things.push(thing);
  }

  var _remove = function (thing) {
    $localStorage.things.splice($localStorage.things.indexOf(thing), 1);
  }

  return {
    getAll: _getAll,
    add: _add,
    remove: _remove
  };
})

.controller('MyCtrl', function($scope,$http,$ionicLoading,$state,StorageService){

  $scope.init = function(){
	window.localStorage.removeItem('Hello');
	 /*
        $http.get("adresse fichier json")
            .success(function(data) {
                items=data;
            })
            .error(function(data) {
                alert("ERROR");
            })
	*/
  // à remplacer par requête http ci-dessus
	var items = [{
						"id":"0001",
						"nom":"Matin",
						"prenom":"Martin",
						"age": 12,
						"classe":"CE2",
						"E1":"",
						"S1":"",
						"E2":"",
						"S2":""
					},
					{
						"id":"0002",
						"nom":"Colin",
						"prenom":"Carla",
						"age": 13,
						"classe":"CP",
						"E1":"",
						"S1":"",
						"E2":"",
						"S2":""
					},
					{
						"id":"0006",
						"nom":"Dupuis",
						"prenom":"Louis",
						"age": 6,
						"classe":"CM2",
						"E1":"",
						"S1":"",
						"E2":"",
						"S2":""
					},
					
					{
						"id":"0003",
						"nom":"Dupont",
						"prenom":"Noemie",
						"age": 8,
						"classe":"CP",
						"E1":"",
						"S1":"",
						"E2":"",
						"S2":""
					},
					{
						"id":"0004",
						"nom":"Menier",
						"prenom":"Elodie",
						"age": 8,
						"classe":"CP",
						"E1":"",
						"S1":"",
						"E2":"",
						"S2":""
					},
					{
						"id":"0005",
						"nom":"Marin",
						"prenom":"David",
						"age": 11,
						"classe":"CP",
						"E1":"",
						"S1":"",
						"E2":"",
						"S2":""
					}
		];
		alert('ok');
	window.localStorage.setItem('Hello',JSON.stringify(items));  
	$scope.enfants = JSON.parse(window.localStorage.getItem('Hello'));
	alert('perfect');
  }
  
  
  $scope.arriver = function(item) {
	var date = new Date();
	alert('Arrivée de '+ item.nom + ' à '+ date.getHours()+"h "+date.getMinutes()+"min "+date.getSeconds()+"s");
	if (item.E1 == ""){
		item.E1=date;
	}else if(item.E2==""){
		item.E2=date;
	}else{
		alert('Trop de pointage');
	}
	window.localStorage.setItem('Hello',JSON.stringify($scope.enfants)); 
	$scope.enfants = JSON.parse(window.localStorage.getItem('Hello'));
  };
  $scope.sortir = function(item) {
	var date = new Date();
    alert('Sortie de '+ item.nom + ' à '+ date.getHours()+"h "+date.getMinutes()+"min "+date.getSeconds()+"s");
	if (item.S1 == ""){
		item.S1=date;
	}else if(item.S2==""){
		item.S2=date;
	}else{
		alert('Trop de pointage');
	}
  };
  
  $scope.plus = function(item) {
	var nom=item.nom
	var prenom=item.prenom
	var age=item.age
	var classe=item.classe
	var E1=item.E1
	var E2=item.E2
	var S1=item.S1
	var S2=item.S2
	$state.go('fiche',{nom : nom, prenom : prenom, age : age, classe : classe, E1 : E1, E2 : E2, S1 : S1, S2 : S2 });
  };
  
  $scope.enfants = JSON.parse(window.localStorage.getItem('Hello'));
  
  $scope.envoyer=function(){
	 /* $http.post("adresse fichier json",data)
            .success(function() {
                alert("ERROR");
            })
            .error(function() {
                alert("ERROR");
            });*/
  }
})

.controller('FicheCtrl', function($scope,$ionicLoading,$state,$stateParams) {
	 $scope.nom = $stateParams.nom;
	 $scope.prenom=$stateParams.prenom;
	 $scope.classe = $stateParams.classe;
	 $scope.age = $stateParams.age;
	 $scope.E1=$stateParams.E1;
	 $scope.S1=$stateParams.S1;
	 $scope.E2=$stateParams.E2;
	 $scope.S2=$stateParams.S2;
})

.config(function($stateProvider,$urlRouterProvider){
		$urlRouterProvider.otherwise('/home')
		$stateProvider
			.state('home',{
			url:'/home',
			templateUrl:'pages/home.html',
			controller : 'MyCtrl'})
			.state('fiche',{
			url:'/fiche/:nom/:prenom/:classe/:age/:E1/:E2/:S1/:S2',
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
