import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";
import { ProveedorAPIService} from '../proveedor-api.service';
import {AngularFirestore} from "@angular/fire/firestore";
import * as firebase from 'firebase';
import { map } from 'rxjs/operators';


@Component({
  selector: 'app-intermediaria',
  templateUrl: './intermediaria.page.html',
  styleUrls: ['./intermediaria.page.scss'],
})
export class IntermediariaPage implements OnInit {
  datos: any = [];
  datos2: any = [];
  docRef;
  volumen: any =[];
  portada: any = [];
  coleccion: any = [];
  datos_volumen: any =[];
  datos_volumen2: any = [];
  datos_pendientes: any = [];
  datos_pendientes2: any = [];
  len_volumenes: any;
  len_pendientes: any;
  constructor(private router: Router, private proveedor: ProveedorAPIService, private db: AngularFirestore) {

    this.datos_volumen =this.proveedor.getVolumen();
    //console.log(this.datos_volumen);
    if(this.datos_volumen.length != 0){
      this.sendVolumen(this.datos_volumen);
    }
    
    this.datos_pendientes =this.proveedor.getVolumen_Pendiente();
    if(this.datos_pendientes.length != 0){
      this.sendPendiente(this.datos_pendientes);
    }
    

    


   }

  ngOnInit() {
    this.proveedor.getVolumenes().subscribe(items =>{
      this.datos_volumen2 = items;
      
      this.proveedor.setDataVolumen(items);
        for(let i in this.datos_volumen2){
          for(let j in this.datos_volumen2[i]){
            this.datos.push(this.datos_volumen2[i][j]);
            this.len_volumenes = this.datos.length;
            this.proveedor.setVolumenesLeidos(this.len_volumenes);
            //console.log(this.datos[0][0])
          }
        }
      });
    

    this.proveedor.getPendientes().subscribe(items =>{
      this.datos_pendientes2 = items;
      
      this.proveedor.setDataPendiente(items);

        for(let i in this.datos_pendientes2){
          for(let j in this.datos_pendientes2[i]){
            this.datos2.push(this.datos_pendientes2[i][j]);
            this.len_pendientes = this.datos2.length;
          }
        }
    });
    

  }

  obtenerColeccion(){
    var user = firebase.auth().currentUser;
    if(this.coleccion.length == 0){
      this.coleccion.push(this.volumen.coleccion);
      this.portada.push(this.volumen.portada);
    }else{
      for(var i=0; i<this.coleccion; i++){
        if(this.coleccion[i]!=this.volumen.coleccion){
          if(this.coleccion[length -1]){
            //this.coleccion.push(this.volumen.coleccion);
            //this.portada.push(this.volumen.portada);
            let docRef =this.db.collection("manga").doc(user.uid).collection("volumenes");
          }
        }else{
          break;
        }
      }
    }
    

  }

  sendVolumen(volumen){
    var user = firebase.auth().currentUser;
    let docRef =this.db.collection("volumenes").doc(user.uid);
    let datos = {volumenes: volumen};
    docRef.set(datos);
   
  }

  sendPendiente(volumen){
    var user = firebase.auth().currentUser;
    let docRef =this.db.collection("pendientes").doc(user.uid);
    let datos = {pendientes: volumen};
    docRef.set(datos);
   
  }
  
  
  getVolumenList(){
    try{

      
      
  }
  catch(error){
    console.log(error);
  }

    

}

}


