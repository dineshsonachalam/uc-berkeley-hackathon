// Step 3: Create reducers for the action types
import {UPDATE_GENDER_STATS, UPDATE_RELATIONSHIP_STATS, UPDATE_ADULT_STATS} from '../actionTypes';

const initialState = { 
    gender_stats: [],
    relationship_stats: [],
    adult_stats: []
};

const genderStatsReducer = (state=initialState, actions) => {
    switch(actions.type) {
        case UPDATE_GENDER_STATS:
            return {...state, gender_stats: actions.payload.gender_stats}
        case UPDATE_RELATIONSHIP_STATS:
            return {...state, relationship_stats: actions.payload.relationship_stats}
        case UPDATE_ADULT_STATS:
            return {...state, adult_stats: actions.payload.adult_stats}
        default:
            return {...state}
    }
}

export default genderStatsReducer;