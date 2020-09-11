import { Component, OnInit } from '@angular/core';
import { ProveedorAPIService} from '../proveedor-api.service';
import { HttpClient} from '@angular/common/http';
@Component({
  selector: 'app-tomo-card-novedades',
  templateUrl: './tomo-card-novedades.page.html',
  styleUrls: ['./tomo-card-novedades.page.scss'],
})
export class TomoCardNovedadesPage implements OnInit {
  id: any;
  datos: any = [];
  tomo_info: any = [];
  tomo_info2: any = [];
  enlace: any;
  enlace2: any;
  res: any;
  constructor(private http: HttpClient, private proveedor: ProveedorAPIService) {
    this.proveedor.obtenerDatosNovedades_Card().subscribe((data) =>{this.tomo_info = data; console.log(this.tomo_info);})
  }

  ngOnInit() {
    
    
  }

  inicializarJSONData(){
    
  }

  



}
