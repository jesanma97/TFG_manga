import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomePage } from './home.page';

const routes: Routes = [
  {
    path: '',
    component: HomePage,
  },
  {
    path: 'search',
    loadChildren: () => import('../search/search.module').then( m => m.SearchPageModule)
  },{
    path: 'novedades',
    loadChildren: () => import('../novedades/novedades.module').then( m => m.NovedadesPageModule)
  },{
    path: 'intermediaria',
    loadChildren: () => import('../intermediaria/intermediaria.module').then( m => m.IntermediariaPageModule)
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class HomePageRoutingModule {}
