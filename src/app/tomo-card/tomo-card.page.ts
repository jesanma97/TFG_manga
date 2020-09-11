import { Component, OnInit } from '@angular/core';
import { ProveedorAPIService} from '../proveedor-api.service';
import { HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-tomo-card',
  templateUrl: './tomo-card.page.html',
  styleUrls: ['./tomo-card.page.scss'],
})
export class TomoCardPage implements OnInit {
  tomo_info: any = [];
  myBoolean: boolean = false;
  myBoolean2: boolean = false;

  constructor(public proveedor: ProveedorAPIService, public http: HttpClient) {
    this.tomo_info = this.proveedor.getData();
    this.tomo_info["anadidoChecked"] = this.myBoolean;
    this.tomo_info["pendienteChecked"] = this.myBoolean2;
   }
  ngOnInit() {
  }

  myBooleanChange(){
    console.log(this.myBoolean);
  }


    
 
  
  }




