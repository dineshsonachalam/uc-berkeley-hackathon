// Step 2: Create Actions for your Action Types

import {UPDATE_GENDER_STATS, UPDATE_RELATIONSHIP_STATS, UPDATE_ADULT_STATS} from './actionTypes';

export const updateGenderStats = (gender_stats) => {
    return {
              type: UPDATE_GENDER_STATS,
              payload: {
                gender_stats: gender_stats
              }
    }
}

export const updateRelationshipStats = (relationship_stats) => {
  return {
            type: UPDATE_RELATIONSHIP_STATS,
            payload: {
              relationship_stats: relationship_stats
            }
  }
}

export const updateAdultStats = (adult_stats) => {
  return {
            type: UPDATE_ADULT_STATS,
            payload: {
              adult_stats: adult_stats
            }
  }
}

