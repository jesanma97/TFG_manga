import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { IntermediariaPageRoutingModule } from './intermediaria-routing.module';

import { IntermediariaPage } from './intermediaria.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    IntermediariaPageRoutingModule
  ],
  declarations: [IntermediariaPage]
})
export class IntermediariaPageModule {}
