import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';
import {AuthGuard} from "./guards/auth.guard";
import {NologinGuard} from "./guards/nologin.guard";

const routes: Routes = [
  {
    path: 'home',
    loadChildren: () => import('./home/home.module').then( m => m.HomePageModule),canActivate : [AuthGuard]
  },
  {
    path: '',
    redirectTo: 'login',
    pathMatch: 'full'
  },
  {
    path: 'estadisticas',
    loadChildren: () => import('./estadisticas/estadisticas.module').then( m => m.EstadisticasPageModule)
  },
  {
    path: 'challenge',
    loadChildren: () => import('./challenge/challenge.module').then( m => m.ChallengePageModule)
  },
  {
    path: 'search',
    loadChildren: () => import('./search/search.module').then( m => m.SearchPageModule)
  },
  {
    path: 'coleccion-card',
    loadChildren: () => import('./coleccion-card/coleccion-card.module').then( m => m.ColeccionCardPageModule)
  },
  {
    path: 'lista-tomos',
    loadChildren: () => import('./lista-tomos/lista-tomos.module').then( m => m.ListaTomosPageModule)
  },
  {
    path: 'tomo-card',
    loadChildren: () => import('./tomo-card/tomo-card.module').then( m => m.TomoCardPageModule)
  },
  {
    path: 'login',
    loadChildren: () => import('./login/login.module').then( m => m.LoginPageModule), canActivate : [NologinGuard]
  },

  {
    path: 'registro',
    loadChildren: () => import('./registro/registro.module').then( m => m.RegistroPageModule), canActivate: [NologinGuard]
  },
  {
    path: 'novedades',
    loadChildren: () => import('./novedades/novedades.module').then( m => m.NovedadesPageModule)
  },
  {
    path: 'tomo-card-novedades',
    loadChildren: () => import('./tomo-card-novedades/tomo-card-novedades.module').then( m => m.TomoCardNovedadesPageModule)
  },
  {
    path: 'intermediaria',
    loadChildren: () => import('./intermediaria/intermediaria.module').then( m => m.IntermediariaPageModule)
  },
  {
    path: 'mis-volumenes',
    loadChildren: () => import('./mis-volumenes/mis-volumenes.module').then( m => m.MisVolumenesPageModule)
  },
  {
    path: 'mis-volumenes-card',
    loadChildren: () => import('./mis-volumenes-card/mis-volumenes-card.module').then( m => m.MisVolumenesCardPageModule)
  },
  {
    path: 'mispendientes',
    loadChildren: () => import('./mispendientes/mispendientes.module').then( m => m.MispendientesPageModule)
  },
  {
    path: 'miscolecciones',
    loadChildren: () => import('./miscolecciones/miscolecciones.module').then( m => m.MiscoleccionesPageModule)
  },
  {
    path: 'miscolecciones-card',
    loadChildren: () => import('./miscolecciones-card/miscolecciones-card.module').then( m => m.MiscoleccionesCardPageModule)
  },
  
  
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
