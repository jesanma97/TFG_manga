import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ColeccionCardPageRoutingModule } from './coleccion-card-routing.module';

import { ColeccionCardPage } from './coleccion-card.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ColeccionCardPageRoutingModule,
  ],
  declarations: [ColeccionCardPage]
})
export class ColeccionCardPageModule {}
