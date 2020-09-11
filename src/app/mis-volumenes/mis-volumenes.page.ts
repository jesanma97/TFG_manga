import { Component, OnInit } from '@angular/core';
import { ProveedorAPIService } from '../proveedor-api.service';

@Component({
  selector: 'app-mis-volumenes',
  templateUrl: './mis-volumenes.page.html',
  styleUrls: ['./mis-volumenes.page.scss'],
})
export class MisVolumenesPage implements OnInit {

  form: any = [];
  tomos_list: any = [];
  volumenes: any = [];
  constructor(public proveedor: ProveedorAPIService) {
    this.tomos_list = this.proveedor.getDataVolumen();
    for(let i in this.tomos_list){
      for(let j in this.tomos_list[i]){
        this.volumenes.push(this.tomos_list[i][j]);
      }
    }
  }

  ngOnInit() {
  }
  
  


}
