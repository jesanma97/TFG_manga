import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ListaTomosPageRoutingModule } from './lista-tomos-routing.module';

import { ListaTomosPage } from './lista-tomos.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ListaTomosPageRoutingModule
  ],
  declarations: [ListaTomosPage]
})
export class ListaTomosPageModule {}
