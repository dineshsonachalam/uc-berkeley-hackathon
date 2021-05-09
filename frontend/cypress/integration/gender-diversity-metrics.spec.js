describe("Search kings", () => {
    it('Load search page', () => {
        cy.visit("http://localhost:3000")
    })

    it('Compare employee details', () => {
        // cy.wait(10000)
        let expected_adult_data = [
            {
                "age": "39",
                "education": "Bachelors",
                "marital_status": "Never-married",
                "native_country": "United-States",
                "salary": "<=50K",
                "gender": "Male"
            },
            {
                "age": "50",
                "education": "Bachelors",
                "marital_status": "Married-civ-spouse",
                "native_country": "United-States",
                "salary": "<=50K",
                "gender": "Male"
            },
            {
                "age": "38",
                "education": "HS-grad",
                "marital_status": "Divorced",
                "native_country": "United-States",
                "salary": "<=50K",
                "gender": "Male"
            },
        ];
        for (var index=0; index < expected_adult_data.length; index++) {   
            const index_pos = index;
            cy.get(`.ant-table-tbody > :nth-child(${index_pos+1}) > :nth-child(1)`).then(($age_elem) => {
                let age = $age_elem.text();
                let expected_age =  expected_adult_data[index_pos]["age"];
                expect(age).to.deep.eq(expected_age);
            })
            cy.get(`.ant-table-tbody > :nth-child(${index_pos+1}) > :nth-child(2)`).then(($education_elem) => {
                let education = $education_elem.text();
                let expected_education =  expected_adult_data[index_pos]["education"];
                expect(education).to.deep.eq(expected_education);
            })
            cy.get(`.ant-table-tbody > :nth-child(${index_pos+1}) > :nth-child(3)`).then(($marital_status_elem) => {
                let marital_status = $marital_status_elem.text();
                let expected_marital_status =  expected_adult_data[index_pos]["marital_status"];
                expect(marital_status).to.deep.eq(expected_marital_status);
            })
            cy.get(`.ant-table-tbody > :nth-child(${index_pos+1}) > :nth-child(4)`).then(($native_country_elem) => {
                let native_country = $native_country_elem.text();
                let expected_native_country =  expected_adult_data[index_pos]["native_country"];
                expect(native_country).to.deep.eq(expected_native_country);
            })
            cy.get(`.ant-table-tbody > :nth-child(${index_pos+1}) > :nth-child(5)`).then(($salary_elem) => {
                let salary = $salary_elem.text();
                let expected_salary =  expected_adult_data[index_pos]["salary"];
                expect(salary).to.deep.eq(expected_salary);
            })
            cy.get(`.ant-table-tbody > :nth-child(${index_pos+1}) > :nth-child(6)`).then(($gender_elem) => {
                let gender = $gender_elem.text();
                let expected_gender =  expected_adult_data[index_pos]["gender"];
                expect(gender).to.deep.eq(expected_gender);
            })
        }
    })
})
