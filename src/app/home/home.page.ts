import { Component, OnInit } from '@angular/core';
import { Platform } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';
import {AuthService} from "../auth.service";
import {Router} from "@angular/router";
import * as firebase from 'firebase';
import { ProveedorAPIService } from '../proveedor-api.service';
import { AngularFirestore } from '@angular/fire/firestore';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
  usuario: any;
  navigate:any;
  datos_volumen: any = [];
  datos_volumen2: any = [];
  lista_pendientes: any = [];

  constructor(private platform: Platform,
    private splashScreen: SplashScreen,
    private statusBar: StatusBar, public authservice: AuthService, public router: Router, private proveedor: ProveedorAPIService, private db: AngularFirestore) {
     
      this.sideMenu();
      this.initializeApp();

      this.proveedor.getPendientes().subscribe(items =>{
        this.datos_volumen2 = items;
        this.proveedor.setData(items);
          for(let i in this.datos_volumen2){
            for(let j in this.datos_volumen2[i]){
              this.lista_pendientes.push(this.datos_volumen2[i][j]);
              console.log(this.lista_pendientes)
            }
          }
      });
      

  }

  ngOnInit() {
   

  }

  initializeApp() {
    this.platform.ready().then(() => {
      this.statusBar.styleDefault();
      this.splashScreen.hide();
    });
  }

  sideMenu(){
    this.navigate = [
      {
        title : "Inicio",
        url   : "/home",
        icon  : "home-outline"
      },
      {
        title : "Reading Challenge",
        url   : "/challenge",
        icon  : "trophy-outline"
      },

    ]
  }

  public Onlogout(){
    this.authservice.logout();
  }
  public novedades_Page(){
    console.log("funciona");
    this.router.navigate(["/novedades"]);
  }

  public intermediaria_Page(){
    console.log("funciona");
    this.router.navigate(["/intermediaria"]);
  }

  public challenge_Page(){
    this.router.navigate(["/challenge"]);
  }



}
