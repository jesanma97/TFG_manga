import { Component, OnInit } from '@angular/core';
import { ProveedorAPIService } from '../proveedor-api.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-mis-volumenes-card',
  templateUrl: './mis-volumenes-card.page.html',
  styleUrls: ['./mis-volumenes-card.page.scss'],
})
export class MisVolumenesCardPage implements OnInit {
  tomo_info: any = [];
  myBoolean: boolean;

  constructor(public proveedor: ProveedorAPIService, public http: HttpClient) {
    this.tomo_info = this.proveedor.getData();

   }
  ngOnInit() {
  }




}
