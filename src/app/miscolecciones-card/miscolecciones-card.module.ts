import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { MiscoleccionesCardPageRoutingModule } from './miscolecciones-card-routing.module';

import { MiscoleccionesCardPage } from './miscolecciones-card.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    MiscoleccionesCardPageRoutingModule
  ],
  declarations: [MiscoleccionesCardPage]
})
export class MiscoleccionesCardPageModule {}
