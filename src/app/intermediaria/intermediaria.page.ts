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
  colecciones: any = [];
  len_colecciones: any;
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
            this.colecciones = this.obtenerColeccion(this.datos);
            this.len_colecciones = this.colecciones.length;
            this.len_volumenes = this.datos.length;
            this.proveedor.setVolumenesLeidos(this.len_volumenes);
            //console.log(this.datos[0][0])
          }
        }
        this.proveedor.setDataColeccion(this.colecciones);
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

  obtenerColeccion(datos){
    var user = firebase.auth().currentUser;
    for(let i in datos){
      //console.log(datos[i]["titulo"]);
      this.coleccion.push(datos[i]["coleccion"])
    }
    const uniqueSet = new Set(this.coleccion);
    const backToArray = [...uniqueSet];
    console.log(backToArray);
    return backToArray;
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


