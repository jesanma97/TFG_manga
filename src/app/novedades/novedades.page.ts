import { Component, OnInit } from '@angular/core';
import { ProveedorAPIService} from '../proveedor-api.service';
import { HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-novedades',
  templateUrl: './novedades.page.html',
  styleUrls: ['./novedades.page.scss'],
})
export class NovedadesPage implements OnInit {

  datos_novedades: any = [];
  id: any;
  datos: any = [];
  enlace: any;
  enlace2: any;
  res: any;
  constructor(private proveedor: ProveedorAPIService, public http: HttpClient) { 
    this.inicializaJSONData();
  }

  ngOnInit() {
  }

  inicializaJSONData(){
    this.proveedor.obtenerDatosNovedades().subscribe((data)=>{this.datos_novedades = data;},
    (error)=>{console.log(error);})
    
  }

  novedades_Datos(){
    this.datos=this.proveedor.getData();
    this.id = this.datos.tomo;
    this.enlace = "http://127.0.0.1:5002/api/v1/tomos/";
    this.enlace2 = this.id;
    this.res = this.enlace.concat(this.enlace2);

    console.log(this.res);
    return this.http.get(String(this.res));
  }





}
