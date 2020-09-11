import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { TomoCardNovedadesPageRoutingModule } from './tomo-card-novedades-routing.module';

import { TomoCardNovedadesPage } from './tomo-card-novedades.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    TomoCardNovedadesPageRoutingModule
  ],
  declarations: [TomoCardNovedadesPage]
})
export class TomoCardNovedadesPageModule {}
