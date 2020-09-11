import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Router } from '@angular/router';
import { ProveedorAPIService} from '../proveedor-api.service';
import { HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-miscolecciones-card',
  templateUrl: './miscolecciones-card.page.html',
  styleUrls: ['./miscolecciones-card.page.scss'],
})
export class MiscoleccionesCardPage implements OnInit {

  datos: any = [];
  tomos_list: any = [];
  volumenes: any = [];
  volumenes_adquiridos: any;
  titulos_añadidos: any = [];
  titulos_volumenes: any = [];
  volumenes2: any = [];
  numero_tomos: any;
  volumenes_publicados: any;
  valor_progreso: number;
  titulo_colec: any;
  enlace: string;
  enlace2: any;
  res: string;
  tomos_list2: any = [];
  valor_parent: any;

  constructor(private http: HttpClient, private route: ActivatedRoute, private router: Router, private proveedor: ProveedorAPIService) {
    this.inicializaJSONData();
    //console.log(this.datos)
    if(this.numero_tomos == undefined){
      this.numero_tomos = 0;
    }
    this.tomos_list = this.proveedor.getDataVolumen();
    //console.log(this.tomos_list)
    for(let i in this.tomos_list){
      for(let j in this.tomos_list[i]){
        this.volumenes.push(this.tomos_list[i][j]);
      }
    }
    console.log(this.volumenes)
    this.titulo_colec  = this.proveedor.getData();
    for(let i in this.volumenes){
      for(let j in this.volumenes[i]){
        if(this.titulo_colec == this.volumenes[i]["coleccion"]){
          this.tomos_list2.push(this.volumenes[i]);
          const uniqueSet = new Set(this.tomos_list2);
          this.tomos_list2 = [...uniqueSet];
        }
      }
    }
    this.volumenes_adquiridos = this.tomos_list2.length;
    //console.log(this.tomos_list2)

    
    
      /*this.volumenes_publicados = this.volumenes2.length;
      for(let i in this.volumenes){
        for(let j in this.volumenes2){
          if(this.volumenes[i]["titulo"]==this.volumenes2[j]["titulo"]){
            this.numero_tomos = this.numero_tomos + 1;
          }
        }
      }*/
      //console.log(this.volumenes_publicados)
      this.valor_progreso = this.numero_tomos/this.volumenes_publicados;
    
    }
    
   

  ngOnInit() {
    
    
    
  }

  inicializaJSONData(){
    this.proveedor.obtenerDatosColeccion().subscribe((data)=>{
      this.datos = data;
      this.valor_parent = this.datos["tomos_espana"].search("serie");
      this.numero_tomos = this.datos["tomos_espana"].substr(0,this.valor_parent -1);
      console.log(parseInt(this.numero_tomos))
    },
    (error)=>{console.log(error);})
    
  }

  

  inicializaTomosColeccion(){
    this.proveedor.obtenerTomosColecciones().subscribe(data => {
      this.numero_tomos = data;
    })
  }

}
  


