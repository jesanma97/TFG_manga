import { Component, OnInit } from '@angular/core';
import {ProveedorAPIService} from "../proveedor-api.service";

@Component({
  selector: 'app-miscolecciones',
  templateUrl: './miscolecciones.page.html',
  styleUrls: ['./miscolecciones.page.scss'],
})
export class MiscoleccionesPage implements OnInit {
  colecciones: any = [];
  constructor(public proveedor: ProveedorAPIService) {
    this.colecciones = this.proveedor.getDataColeccion();
  }

  ngOnInit() {
  }

}
