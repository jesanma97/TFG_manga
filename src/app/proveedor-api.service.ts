import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import {AngularFirestore} from "@angular/fire/firestore";
import * as firebase from 'firebase';


@Injectable({
  providedIn: 'root'
})
export class ProveedorAPIService {
  public sharedData: any = [];
  public volumenes_leidos: any;
  public volumen_list: any = [];
  public coleccion_list: any = [];
  public pendiente_list: any = [];
  public tomo_info: any = [];
  public volumen: any= [];
  public volumen_Pendiente: any = [];
  public titulo: any;
  public titulo_colec: any;
  public objetivo: any;
  enlace_tomos: string;
  items: any = [];
  items2: any = [];
  datos: any = [];
  id: any;
  enlace: string;
  enlace2: any;
  res: string;
  datos2: any;
  datos3: any;
  result: any;
  
  constructor(private http: HttpClient, private db: AngularFirestore) {
    console.log('Hello Proveedor');
    var user = firebase.auth().currentUser;
    this.items = this.db.collection("volumenes").doc(user.uid).valueChanges();
    this.items2 = this.db.collection("pendientes").doc(user.uid).valueChanges();
   }
  
   public obtenerDatosColecciones(){
     return this.http.get("http://127.0.0.1:5002/api/v1/colecciones");
   }

   public obtenerDatosNovedades(){
     return this.http.get("http://127.0.0.1:5002/api/v1/novedades");
   }
   
   setData(data){
     this.sharedData = data;
   }

   getData(){
     return this.sharedData;
   }

   setDataVolumen(data){
     this.volumen_list = data;
   }
   setDataColeccion(data){
     this.coleccion_list = data;
   }

   getDataColeccion(){
     return this.coleccion_list;
   }

   getDataVolumen(){
     return this.volumen_list;
   }

   setDataPendiente(data){
    this.pendiente_list = data;
   }

   getDataPendiente(){
     return this.pendiente_list;
   }

   setVolumen(data){
     this.volumen.push(data);
   }

   setVolumen_Pendiente(data){
     this.volumen_Pendiente.push(data);
   }

   getVolumen_Pendiente(){

     return this.volumen_Pendiente;
   }

   getVolumen(){

     return this.volumen;
   }

   getVolumenes(){
    return this.items;
   }

   getPendientes(){
     return this.items2;
   }

   /*sendVolumen(volumen){
    var user = firebase.auth().currentUser;
    let docRef =this.db.collection("manga").doc(user.uid);
    let datos = {pendientes: volumen};
    docRef.set(datos);
  }*/
   

   obtenerDatosNovedades_Card(){
    this.datos = this.getData();
    this.id = this.datos.tomo;
    this.enlace = "http://127.0.0.1:5002/api/v1/tomos/";
    this.enlace2 = this.id;
    this.res = this.enlace.concat(this.enlace2);
    return this.http.get(String(this.res));
   }

   obtenerDatosColeccion(){
     this.titulo_colec = this.getData();
     this.titulo_colec = this.titulo_colec.replace(/\s/g,"%20");
     this.enlace = "http://127.0.0.1:5002/api/v1/colecciones/";
     this.enlace2 = this.titulo_colec;
     this.res = this.enlace.concat(this.enlace2);
     return this.http.get(String(this.res));
   }

   obtenerTomosColecciones(){
    this.titulo_colec = this.getData();
    this.titulo_colec = this.titulo_colec.replace(/\s/g,"%20");
    this.enlace = "http://127.0.0.1:5002/api/v1/num_tomos/";
    this.enlace2 = this.titulo_colec;
    this.res = this.enlace.concat(this.enlace2);
    console.log(this.res)
    return this.http.get(String(this.res));
   }

   
   setVolumenesLeidos(data){
    this.volumenes_leidos = data;
    
   }

   getVolumenesLeidos(){
     return this.volumenes_leidos;
   }

   setObjetivoVolumenes(data){
    this.objetivo = data;
   }

   getObjetivoVolumenes(){
     return this.objetivo;
   }

   setDataConjunto(data){
     this.sharedData = data;
   }

   getDataConjunto(){
     return this.sharedData;
   }

   

}
