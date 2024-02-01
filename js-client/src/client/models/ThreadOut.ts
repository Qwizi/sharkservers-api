/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { Category_AHN } from './Category_AHN';
import type { Server_FJT } from './Server_FJT';
import type { ThreadMeta_TNX } from './ThreadMeta_TNX';
import type { User_PRS } from './User_PRS';

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
    category?: Category_AHN;
    author?: User_PRS;
    meta_fields?: Array<ThreadMeta_TNX>;
    post_count?: number;
    server?: Server_FJT;
};

