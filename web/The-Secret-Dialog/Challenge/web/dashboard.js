// Dialog Frontend Hydration State Bundle v2.4.11
// Production Build - Webpack Compiled

window.__NEXT_DATA__ = {
    props: {
        pageProps: {
            session: {
                status: "unauthenticated",
                requiredClearance: "Omega-Level"
            },
            // Das kritische Daten-Leak aus der Datenbank:
            leakedDirectoryData: {
                node: "Silicon-Valley-Mainframe",
                totalMembers: 4,
                vipList: [
                    { name: "P. Tee", role: "Founder", state: "Active" },
                    { name: "E. Muskateller", role: "Member", state: "Active" },
                    { name: "M. Zuckerthal", role: "Guest", state: "Pending" }
                ],
                // Die Flagge liegt tief im unverschlüsselten Frontend-Speicherobjekt!
                systemSecretFlag: "CLA{j4v45cr1p7_bundl35_4r3_publ1c_f1l35}"
            }
        }
    }
};

console.log("[Dialog System] Hydration completed. Session state evaluated: Unauthorized.");