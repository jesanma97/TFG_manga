import { Component } from '@angular/core';

import { Platform } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';
import {AuthService} from "./auth.service";
import * as firebase from 'firebase';


@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss']
})
export class AppComponent {
  navigate:any;
  usuario: any;
  constructor(
    private platform: Platform,
    private splashScreen: SplashScreen,
    private statusBar: StatusBar, private proveedor: AuthService
  ) {
    
    this.sideMenu();
    this.initializeApp();
    
  
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
    this.proveedor.logout();
  }

  // Query for the toggle that is used to change between themes

}
