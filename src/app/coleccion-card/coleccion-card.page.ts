import { Component, OnInit, ɵConsole } from '@angular/core';
import {ActivatedRoute, Router } from '@angular/router';
import { ProveedorAPIService} from '../proveedor-api.service';
import { HttpClient} from '@angular/common/http';


@Component({
  
  selector: 'app-coleccion-card',
  templateUrl: './coleccion-card.page.html',
  styleUrls: ['./coleccion-card.page.scss'],
})
export class ColeccionCardPage implements OnInit {
  datos_colec_card: any = [];
  tomos: any = [];
  titulo: any;
  enlace: string;
  enlace2: string;
  public res:string;
  
  constructor(private http: HttpClient, private route: ActivatedRoute, private router: Router, private proveedor: ProveedorAPIService ) {
    this.inicializaJSONData();
  
  }
    

  ngOnInit() {
    
   
  }
  public obtenerDatosTomosImgs(){
    this.datos_colec_card=this.proveedor.getData();
    this.titulo = this.datos_colec_card.titulo;
    this.titulo = this.titulo.replace(/\s/g,"%20");
    this.enlace = "http://127.0.0.1:5002/api/v1/tomos/";
    this.enlace2 = this.titulo;
    this.res = this.enlace.concat(this.enlace2);

    console.log(this.res);
    return this.http.get(String(this.res));
  }

  inicializaJSONData(){
    this.obtenerDatosTomosImgs().subscribe((data)=>{this.tomos = data;this.proveedor.setData(this.tomos);},
    (error)=>{console.log(error);})
    
  }

  


}
