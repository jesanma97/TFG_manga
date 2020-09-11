import { TestBed } from '@angular/core/testing';

import { Proveedor2Service } from './proveedor2.service';

describe('Proveedor2Service', () => {
  let service: Proveedor2Service;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Proveedor2Service);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
