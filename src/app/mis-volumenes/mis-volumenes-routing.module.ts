import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { MisVolumenesPage } from './mis-volumenes.page';

const routes: Routes = [
  {
    path: '',
    component: MisVolumenesPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class MisVolumenesPageRoutingModule {}
