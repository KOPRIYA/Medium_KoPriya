public class TechPolicyService {

    public static boolean validate(String techStack) {
        return !techStack.contains("experimental");
    }
}