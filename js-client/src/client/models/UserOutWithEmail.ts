/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { Ban_ATT } from './Ban_ATT';
import type { Like_FNC } from './Like_FNC';
import type { Player_LPL } from './Player_LPL';
import type { Post_EHQ } from './Post_EHQ';
import type { Role_HOY } from './Role_HOY';
import type { Thread_EKU } from './Thread_EKU';
import type { UserSession_GIS } from './UserSession_GIS';

/**
 * Represents the output schema for a user with email.
 */
export type UserOutWithEmail = {
    created_at?: string;
    updated_at?: string;
    id?: number;
    username: string;
    email: string;
    is_activated?: boolean;
    is_superuser?: boolean;
    avatar?: string;
    roles?: Array<Role_HOY>;
    display_role?: Role_HOY;
    last_login?: string;
    last_online?: string;
    threads_count?: number;
    posts_count?: number;
    likes_count?: number;
    player?: Player_LPL;
    sessions?: Array<UserSession_GIS>;
    banned_user?: Array<Ban_ATT>;
    banned_by?: Array<Ban_ATT>;
    user_reputation?: Array<Like_FNC>;
    user_posts?: Array<Post_EHQ>;
    user_threads?: Array<Thread_EKU>;
};

