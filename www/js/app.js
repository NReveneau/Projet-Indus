// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
angular.module('MyApp', ['ionic', 'ngStorage'])

//Le controlleur de la page principale
.controller('MyCtrl', function($scope,$http,$ionicLoading,$state){

//Fonction correspondant au bouton "Mise à jour",
// servant à charger la liste d'enfants et la stocker en locale
  $scope.init = function(){
	window.localStorage.removeItem('Hello');
	
	//à implémenter dès que la liaison sera prête côté application web
	 /*
		var items;
        $http.get("adresse fichier json")
            .success(function(data) {
                items=data;
            })
            .error(function(data) {
                alert("ERROR");
            })
	*/
  // tableau test à remplacer par requête http ci-dessus
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
	window.localStorage.setItem('Hello',JSON.stringify(items)); //stockage du tableau items sous format JSON sous la variable 'Hello' 
	$scope.enfants = JSON.parse(window.localStorage.getItem('Hello'));
  }
  
//Fonction relative au bouton "arrivée",
// pour enregistrer l'heure d'arrivée de l'enfant 
  $scope.arriver = function(item) {
	var date = new Date();
	if (item.E1 == ""){
		if(date.getMinutes()<10)item.E1=date.getHours()+":0"+date.getMinutes()+":00";
		else item.E1=date.getHours()+":"+date.getMinutes()+":00";
	}else if(item.E2==""){
		if(date.getMinutes()<10)item.E2=date.getHours()+":0"+date.getMinutes()+":00";
		else item.E2=date.getHours()+":"+date.getMinutes()+":00";
	}else{
		alert('Trop de pointage'); //POPUP //en cas de pointage de trop !
	}
	window.localStorage.setItem('Hello',JSON.stringify($scope.enfants)); 
	$scope.enfants = JSON.parse(window.localStorage.getItem('Hello'));
  };
  
 //Fonction relative au bouton "sortie",
// pour enregistrer l'heure de sortie de l'enfant 
  $scope.sortir = function(item) {
	var date = new Date();
	if (item.S1 == ""){
		if(date.getMinutes()<10)item.S1=date.getHours()+":0"+date.getMinutes()+":00";
		else item.S1=date.getHours()+":"+date.getMinutes()+":00";
	}else if(item.S2==""){
		if(date.getMinutes()<10)item.S2=date.getHours()+":0"+date.getMinutes()+":00";
		else item.S2=date.getHours()+":"+date.getMinutes()+":00";
	}else{
		alert('Trop de pointage'); //POPUP //en cas de pointage de trop !
	}
	window.localStorage.setItem('Hello',JSON.stringify($scope.enfants)); 
	$scope.enfants = JSON.parse(window.localStorage.getItem('Hello'));
  };
 //Fonction relative au bouton "voir plus",
// pour pouvoir passer à la fiche de l'enfant 
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
  }
  
  //Variable "enfants" ayant pour contenu la liste enregistrée en locale
  $scope.enfants = JSON.parse(window.localStorage.getItem('Hello'));
  
  //Fonction relative à la mise à jour des modifications pour la visualisation
  $scope.recharger=function(){
	$scope.enfants = JSON.parse(window.localStorage.getItem('Hello'));
  }
  
  
 //Fonction correspondant au bouton "Envoyer les données du jour",
// servant à envoyer les pointage du jour
//à implémenter dès que la liaison sera prête côté application web
  $scope.envoyer=function(){
	 /* $http.post("adresse fichier json",JSON.stringify(JSON.parse(window.localStorage.getItem('Hello'))))
            .success(function() {
                alert("ERROR");
            })
            .error(function() {
                alert("ERROR");
            });*/
  }
})


//Le Controlleur de la page "fiche" enfant
.controller('FicheCtrl', function($scope,$ionicLoading,$state,$stateParams) {

	//ici il s'agit de faire le lien entre les données des 2 pages
	 $scope.nom = $stateParams.nom;
	 $scope.prenom=$stateParams.prenom;
	 $scope.classe = $stateParams.classe;
	 $scope.age = $stateParams.age;
	 $scope.E1=$stateParams.E1;
	 $scope.S1=$stateParams.S1;
	 $scope.E2=$stateParams.E2;
	 $scope.S2=$stateParams.S2;
	 
 //Fonction relative au bouton "modifier",
// pour modifier un pointage ou le supprimer
	 $scope.modifier = function(){
		var tableau = JSON.parse(window.localStorage.getItem('Hello'));
		var horaire = document.getElementById("horaire").value;
		var pointage = document.getElementById('pointage').selectedIndex;
		for (var name in tableau){
		 if ((tableau[name].nom == $scope.nom) && (tableau[name].prenom == $scope.prenom)){ 
			switch(pointage) {
				case 0:
					tableau[name].E1=horaire+":00";
					break;
				case 1:
					tableau[name].S1=horaire+":00";
					break;
				case 2:
					tableau[name].E2=horaire+":00";
					break;
				default:
					tableau[name].S2=horaire+":00";
					break;
			}
		}
		}
		window.localStorage.setItem('Hello',JSON.stringify(tableau));
	 }
})

//Sert à la configuration/au paramétrage pour la navigation entre les différentes pages
.config(function($stateProvider,$urlRouterProvider){
		$urlRouterProvider.otherwise('/home')
		$stateProvider
			.state('home',{
			url:'/home',
			templateUrl:'pages/home.html',
			controller : 'MyCtrl'})
			.state('fiche',{
			url:'/fiche/:nom/:prenom/:classe/:age/:E1/:E2/:S1/:S2',//les éléments suite à la fiche 
																//nécessaires pour la liaison de données
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
