import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { MispendientesPage } from './mispendientes.page';

const routes: Routes = [
  {
    path: '',
    component: MispendientesPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class MispendientesPageRoutingModule {}
