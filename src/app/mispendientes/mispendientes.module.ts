import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { MispendientesPageRoutingModule } from './mispendientes-routing.module';

import { MispendientesPage } from './mispendientes.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    MispendientesPageRoutingModule
  ],
  declarations: [MispendientesPage]
})
export class MispendientesPageModule {}
