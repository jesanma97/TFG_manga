import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { IntermediariaPage } from './intermediaria.page';

const routes: Routes = [
  {
    path: '',
    component: IntermediariaPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class IntermediariaPageRoutingModule {}
