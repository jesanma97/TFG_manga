import { Component, OnInit } from '@angular/core';
import { ProveedorAPIService } from '../proveedor-api.service';

@Component({
  selector: 'app-mispendientes',
  templateUrl: './mispendientes.page.html',
  styleUrls: ['./mispendientes.page.scss'],
})
export class MispendientesPage implements OnInit {

  form: any = [];
  tomos_list: any = [];
  pendientes: any = [];
  constructor(public proveedor: ProveedorAPIService) {
    this.tomos_list = this.proveedor.getDataPendiente();
    for(let i in this.tomos_list){
      for(let j in this.tomos_list[i]){
        this.pendientes.push(this.tomos_list[i][j]);
      }
    }
  }

  ngOnInit() {
  }

}
