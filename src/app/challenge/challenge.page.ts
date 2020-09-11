import { Component, OnInit } from '@angular/core';
import { ProveedorAPIService } from '../proveedor-api.service';
import {AlertController} from "@ionic/angular";

@Component({
  selector: 'app-challenge',
  templateUrl: './challenge.page.html',
  styleUrls: ['./challenge.page.scss'],
})
export class ChallengePage implements OnInit {
  volumenes_leidos: any;
  valor_alert: any;
  res: any;
  valor_progreso: any;
  constructor(public proveedor: ProveedorAPIService, public alertController: AlertController) {
    this.volumenes_leidos=this.proveedor.getVolumenesLeidos();
    if(this.volumenes_leidos == undefined){
      this.volumenes_leidos = 0;
    }
    this.res = this.proveedor.getObjetivoVolumenes();
    if(this.res == undefined){
      this.res = 0;
    }

    

    this.valor_progreso = this.volumenes_leidos/this.res;
    if(this.res == 0){
      this.valor_progreso = 0;
    }
    console.log(this.volumenes_leidos);
   }


  ngOnInit() {
  }

  async presentAlertPrompt(){
    const alert = await this.alertController.create({
      header: "Objetivo a cumplir",
      inputs:[{
        name:"valor",
        type:"number",
        placeholder:"Introduce el número de tomos a leer"
      }],
      buttons:[{
        text: 'Cancelar',
        role: 'cancel',
        cssClass:'danger',
        handler:() =>{
          console.log("Confirm cancel")
        }
      },
      {
        text: 'OK',
        cssClass:'primary',
        handler:() =>{
          console.log("Confirm OK")
        }
      }]
    });
    await alert.present();
    let result = await alert.onDidDismiss();
    this.valor_alert = result.data.values.valor;
    this.proveedor.setObjetivoVolumenes(this.valor_alert);
    console.log(this.valor_alert);
    console.log(result);
  }

}
