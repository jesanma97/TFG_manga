import { Component, OnInit } from '@angular/core';
import { ProveedorAPIService} from '../proveedor-api.service';

@Component({
  selector: 'app-lista-tomos',
  templateUrl: './lista-tomos.page.html',
  styleUrls: ['./lista-tomos.page.scss'],
})
export class ListaTomosPage implements OnInit {
  form: any = [];
  tomos_list: any [] = [];
  myBoolean: boolean;
  isOdd = false;
  constructor(public proveedor: ProveedorAPIService) {
    this.tomos_list = this.proveedor.getData();
    for(var i=0;i<this.tomos_list.length;i++){
      this.tomos_list[i]["isChecked"]=this.myBoolean;
    }
    
  
  }

  ngOnInit() {
  }
  
  

  myBooleanChange(item){
    console.log(this.myBoolean);
  }
 
  public get changeOdd(){
    this.isOdd = !this.isOdd;
    return true;
  }

}
