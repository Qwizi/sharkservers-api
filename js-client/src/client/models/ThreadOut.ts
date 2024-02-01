/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { Category_IHZ } from './Category_IHZ';
import type { Server_CLS } from './Server_CLS';
import type { ThreadMeta_SKI } from './ThreadMeta_SKI';
import type { User_TAE } from './User_TAE';

/**
 * Thread output schema.
 */
export type ThreadOut = {
    created_at?: string;
    updated_at?: string;
    id?: number;
    title: string;
    content: string;
    is_closed?: boolean;
    is_pinned?: boolean;
    status?: string;
    category?: Category_IHZ;
    author?: User_TAE;
    meta_fields?: Array<ThreadMeta_SKI>;
    post_count?: number;
    server?: Server_CLS;
};

