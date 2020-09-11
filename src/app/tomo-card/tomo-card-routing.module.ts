import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { TomoCardPage } from './tomo-card.page';

const routes: Routes = [
  {
    path: '',
    component: TomoCardPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class TomoCardPageRoutingModule {}
