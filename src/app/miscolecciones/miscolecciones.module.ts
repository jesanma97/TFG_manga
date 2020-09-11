import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { MiscoleccionesPageRoutingModule } from './miscolecciones-routing.module';

import { MiscoleccionesPage } from './miscolecciones.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    MiscoleccionesPageRoutingModule
  ],
  declarations: [MiscoleccionesPage]
})
export class MiscoleccionesPageModule {}
